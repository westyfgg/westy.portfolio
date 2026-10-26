from django.db import migrations, models
import django.db.models.deletion


def create_defaults(apps, schema_editor):
    SiteProfile = apps.get_model("links", "SiteProfile")
    ProfileLink = apps.get_model("links", "ProfileLink")
    profile, _ = SiteProfile.objects.using(schema_editor.connection.alias).get_or_create(
        pk=1,
        defaults={
            "display_name": "WESTY",
            "username": "@WESTY",
            "quote": "«Роби з душею — і результат говоритиме сам за себе.»",
            "avatar_url": "",
        },
    )
    titles = (
        "My Telegram",
        "TikTok",
        "Info",
        "Stars",
        "Telegram Premium",
        "Price",
        "Contact me",
    )
    for sort_order, title in enumerate(titles, start=1):
        ProfileLink.objects.using(schema_editor.connection.alias).get_or_create(
            profile_id=profile.pk,
            title=title,
            defaults={"url": "", "sort_order": sort_order, "is_active": True},
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("display_name", models.CharField(default="WESTY", max_length=80, verbose_name="Display name")),
                ("username", models.CharField(default="@WESTY", max_length=80, verbose_name="Username")),
                (
                    "quote",
                    models.CharField(
                        blank=True,
                        default="«Роби з душею — і результат говоритиме сам за себе.»",
                        max_length=180,
                        verbose_name="Quote shown below your name",
                    ),
                ),
                ("avatar_url", models.URLField(blank=True, verbose_name="Avatar image URL")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
            ],
            options={
                "verbose_name": "Profile and links",
                "verbose_name_plural": "Profile and links",
            },
        ),
        migrations.CreateModel(
            name="ProfileLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=60, verbose_name="Button title (English)")),
                ("url", models.URLField(blank=True, verbose_name="Link URL")),
                ("sort_order", models.PositiveSmallIntegerField(default=0, verbose_name="Display order")),
                ("is_active", models.BooleanField(default=True, verbose_name="Show on page")),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="links.siteprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Page link",
                "verbose_name_plural": "Page links",
                "ordering": ("sort_order", "id"),
            },
        ),
        migrations.RunPython(create_defaults, migrations.RunPython.noop),
    ]
