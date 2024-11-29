from celery import shared_task
from django.core.mail import send_mail
from .models import Todo, User
@shared_task
def send_welcome_email(email):
    subject = "Welcome to Todos App"
    message = "Thank you for registering! We're excited to have you on board."
    from_email = "no-reply@todosapp.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Welcome email sent to {email}"

@shared_task
def send_reminder_emails():
    users_with_pending_todos = User.objects.filter(
        todo__status='pending'
    ).distinct()
    for user in users_with_pending_todos:
        pending_todos = Todo.objects.filter(user=user, status='pending')
        todo_titles = "\n".join([f"- {todo.title}" for todo in pending_todos])

        subject = "Reminder: You have pending to-dos"
        message = (
            f"Hello {user.username},\n\n"
            f"You have the following pending to-dos:\n"
            f"{todo_titles}\n\n"
            f"Please complete them as soon as possible!\n\n"
            f"Best regards,\nYour To-Do App"
        )
        from_email = "no-reply@todosapp.com"
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

    return f"Reminder emails sent to {users_with_pending_todos.count()} users."