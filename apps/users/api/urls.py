from rest_framework.routers import DefaultRouter

from apps.users.api.views.account import Account
from apps.users.api.views.auth import (
    AccountActivation,
    EmailChange,
    EmailChangeVerify,
    Login,
    Logout,
    PasswordChange,
    PasswordReset,
    PasswordResetVerify,
    SignUp,
)

router = DefaultRouter()
router.register(r"account", Account, basename="account")
router.register(r"login", Login, basename="login")
router.register(r"logout", Logout, basename="logout")
router.register(r"signup", SignUp, basename="signup")
router.register(r"activate", AccountActivation, basename="account_activation")
router.register(r"password-change", PasswordChange, basename="password_change")
router.register(r"password-reset", PasswordReset, basename="password_reset")
router.register(r"password-reset-verify", PasswordResetVerify, basename="password_reset_verify")
router.register(r"email-change", EmailChange, basename="email_change")
router.register(r"email-change-verify", EmailChangeVerify, basename="email_change_verify")

urlpatterns = router.urls
