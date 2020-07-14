from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmEmailTokenGenerator(PasswordResetTokenGenerator):
    def make_hash_value(self, user, timestamp):
        return str(user.pk) + str(user.is_active) + str(timestamp)
