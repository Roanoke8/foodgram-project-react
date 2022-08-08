class SubscribeMixin:

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return (
            user.is_authenticated
            and user.follower.filter(author=obj).exists()
        )
