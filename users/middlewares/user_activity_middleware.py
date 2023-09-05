from users.models import UserActivity


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Capture user activities here
            action = f"Visited {request.path}"
            UserActivity.objects.create(user=request.user, action=action)
        response = self.get_response(request)

        return response
