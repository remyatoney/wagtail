from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    """Home page model."""

    templates = "templates/home/home_page.html" # Specified the template for the homepage
    max_count = 1 # Specifies that only 1 home page is allowed

    banner_title = models.CharField(max_length=100, blank=False, null=True) # Creates a column called banner_title in homepage table
    banner_subtitle = RichTextField(features=["bold", "italic"]) # Richtext field allows this column to be customized to have bold or italic font
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ] # Makes banner title field editable in the admin panel

    class Meta:

        verbose_name = "Home Page" # Calls the page Home Page (same as default)
        verbose_name_plural = "Home Pages"