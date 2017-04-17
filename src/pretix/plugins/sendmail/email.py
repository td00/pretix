from pretix.base.email import MailTemplateRenderer

mail_text_sendmail = MailTemplateRenderer(
    ['due_date', 'event', 'order', 'order_date', 'order_url', 'invoice_name', 'invoice_company']
)
