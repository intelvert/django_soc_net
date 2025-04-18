from datetime import timedelta
from django.utils.timezone import now

def is_editable(user, obj, hours):
    """Checks if User can edit a Post.

    Args:
        user: User, who tries to edit.
        obj: Object with 'author', 'created_at' attributes.
        hours: Time period during which Post can be edited.

    Returns:
        Tuple (bool, str): True and empty string if editing is allowed.
                           False and error message if not."""
                           
    model_name=obj._meta.model_name.capitalize()
    
    if obj.author!=user:
        return False, f"You are not allowed to edit this {model_name}."
    
    edit_time=now()-timedelta(hours=hours)
    if obj.created_at<edit_time:
        return False, f"You cannot edit a {model_name} that was created more than an hour ago."
    
    return True, ""