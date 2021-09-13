
"""Flexible page"""
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class FlexPage(Page):
    """Flexible page class"""

    # @todo add streamfields
    # content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name= "Flex Page"
        verbose_name_plural = "Flex pages"