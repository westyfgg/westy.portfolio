from django.db import migrations


OLD_QUOTE = "Роби з душею — і результат говоритиме сам за себе."
NEW_QUOTE = "«Роби з душею — і результат говоритиме сам за себе.»"


def add_quotation_marks(apps, schema_editor):
    SiteProfile = apps.get_model("links", "SiteProfile")
    SiteProfile.objects.using(schema_editor.connection.alias).filter(
        quote=OLD_QUOTE
    ).update(quote=NEW_QUOTE)


class Migration(migrations.Migration):
    dependencies = [("links", "0001_initial")]

    operations = [
        migrations.RunPython(add_quotation_marks, migrations.RunPython.noop),
    ]
