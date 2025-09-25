from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام", help_text="")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس", help_text="")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل", help_text="")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ایجاد", help_text=""
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال",
        help_text="اگر تیک خورده باشد، مخاطب فعال است",
    )
    not_activated = models.BooleanField(
        default=False,
        verbose_name="غیرفعال شده",
        help_text="اگر تیک خورده باشد، مخاطب هنوز فعال نشده است",
    )

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        ordering = ["name"]
        verbose_name = "مخاطب"
        verbose_name_plural = "مخاطبین"
