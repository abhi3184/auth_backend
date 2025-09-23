from fastapi import APIRouter
from models.index import UserTable
from schemas.index import User,UserLogin,EmailOTPRequest,MobileOTPRequest,EmailOTPVerifyRequest,UpdatePasswordReq,VerifyEmailOTPRequest,VerifyMobileOTPRequest
from fastapi import APIRouter
from services.index import ForgotPasswordService

forgotPass = APIRouter()

@forgotPass.post("/send-email-otp")
async def send_email_otp(payload: EmailOTPRequest):
    return ForgotPasswordService.send_email_otp(payload)

@forgotPass.post("/verify-email-otp")
async def verify_email_otp(payload: EmailOTPVerifyRequest):
    result = ForgotPasswordService.verify_email_otp(payload)
    return result

@forgotPass.post("/send-mobile-otp")
async def send_mobile_otp(payload: MobileOTPRequest):
    return ForgotPasswordService.send_mobile_otp(payload)

@forgotPass.post("/verify-otp")
async def verify_mobile_otp(payload: VerifyMobileOTPRequest):
    result = ForgotPasswordService.verify_mobile_otp(payload)
    return result

@forgotPass.post("/resend-email-otp")
async def resend_email_otp(payload: EmailOTPRequest):
    return ForgotPasswordService.resend_email_otp(payload)

@forgotPass.post("/resend-mobile-otp")
async def resend_mobile_otp(payload: MobileOTPRequest):
    return ForgotPasswordService.resend_mobile_otp(payload)
    
@forgotPass.put("/update-password")
async def update_password(req:UpdatePasswordReq):
    return ForgotPasswordService.update_password(req)