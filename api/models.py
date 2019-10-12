from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# from django.core.exceptions import ValidationError

# Create your models here.


class Takhasos(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class SentenceStatus(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class JudgmentsStatus(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class ContentType(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class FileGallery(models.Model):
    title = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to='media/upload/files')

    def __str__(self):
        return self.title


class PaymentStatus(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class Sentence(models.Model):
    title = models.CharField(max_length=100)
    takhasos = models.ForeignKey(Takhasos, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    mohlat_rooz = models.IntegerField()
    mohlat_saat = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(SentenceStatus, on_delete=models.DO_NOTHING)
    word_count = models.IntegerField()
    zemanat_price = models.DecimalField(decimal_places=0, max_digits=10)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    # content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    content_text = models.TextField(max_length=500)

    # content_file = models.FileField(upload_to='media/upload/sentence_files', blank=True)
    translator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='translator')
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.DO_NOTHING, null=True, default=1)

    def __str__(self):
        return 'Time: %s, %s' % (self.create_time, self.title)

    class Meta:
        ordering = ('-id',)



class SuggestStatus(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Suggest(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    mojri = models.ForeignKey(User, on_delete=models.CASCADE)
    # zaman_pishnahadi = models.IntegerField()
    mablagh_pishnahadi = models.DecimalField(decimal_places=0, max_digits=10)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=True)
    status = models.ForeignKey(SuggestStatus, on_delete=models.DO_NOTHING)
    completeFile = models.FileField(null=True, upload_to='media/upload/Content_File_Of_Suggest')
    upload_time = models.DateTimeField(null=True, blank=True)
    rate_number = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.sentence.title


class Judgment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    judgment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    judgment_description = models.TextField(blank=True, max_length=500)
    suggest = models.ForeignKey(Suggest, on_delete=models.CASCADE)
    judgment_won_user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                          null=True, related_name='won_user')
    davar_description = models.TextField(blank=True, max_length=500)
    mablagh = models.DecimalField(decimal_places=0, max_digits=10, default=0)
    status = models.ForeignKey(JudgmentsStatus, null=True, on_delete=models.DO_NOTHING)


class UserType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UserStatus(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Maharat(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    mojodi = models.DecimalField(decimal_places=0, max_digits=10)
    mobile = models.CharField(max_length=11, blank=True)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    user_status = models.ForeignKey(UserStatus, on_delete=models.DO_NOTHING)
    resume_description = models.TextField(max_length=500)
    resume_file = models.ForeignKey(FileGallery, on_delete=models.DO_NOTHING, blank=True, null=True)
    # maharat = models.ManyToManyField(Maharat, blank=True)
    rate = models.DecimalField(decimal_places=2, max_digits=3)


class Payment(models.Model):
    amount = models.IntegerField()
    authority = models.CharField(max_length=36)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(blank=True, null=True)
    ref_id = models.CharField(max_length=100, blank=True)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)

    def __str__(self):
        return 'user={0}, time={1}'.format(self.dashboard.user, self.create_time)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)