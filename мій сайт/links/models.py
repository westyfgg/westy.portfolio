from django.db import models


class SiteProfile(models.Model):
    display_name = models.CharField("Display name", max_length=80, default="WESTY")
    username = models.CharField("Username", max_length=80, default="@WESTY")
    quote = models.CharField(
        "Quote shown below your name",
        max_length=180,
        blank=True,
        default="«Роби з душею — і результат говоритиме сам за себе.»",
    )
    avatar_url = models.URLField("Avatar image URL", blank=True)
    updated_at = models.DateTimeField("Updated", auto_now=True)

    class Meta:
        verbose_name = "Profile and links"
        verbose_name_plural = "Profile and links"

    def __str__(self):
        return self.display_name

    @classmethod
    def get_profile(cls):
        profile, _ = cls.objects.get_or_create(pk=1)
        return profile


class ProfileLink(models.Model):
    profile = models.ForeignKey(
        SiteProfile,
        on_delete=models.CASCADE,
        related_name="links",
    )
    title = models.CharField("Button title (English)", max_length=60)
    url = models.URLField("Link URL", blank=True)
    sort_order = models.PositiveSmallIntegerField("Display order", default=0)
    is_active = models.BooleanField("Show on page", default=True)

    class Meta:
        ordering = ("sort_order", "id")
        verbose_name = "Page link"
        verbose_name_plural = "Page links"

    def __str__(self):
        return self.title
