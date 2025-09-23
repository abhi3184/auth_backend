from fastapi import APIRouter
from schemas.index import User,EmailOTPRequest,MobileOTPRequest,VerifyEmailOTPRequest,VerifyMobileOTPRequest
from fastapi import APIRouter
from services.index import userRegistrationService

registration = APIRouter()

reg_otp_store = {} 
@registration.post("/send-email-otp")
async def send_email_otp(payload: EmailOTPRequest):
    return userRegistrationService.send_email_otp(payload)
    
@registration.post("/verify-email-otp")
async def verify_email_otp(payload: VerifyEmailOTPRequest):   
    return userRegistrationService.verify_email_otp(payload)

@registration.post("/resend-email-otp")
async def resend_email_otp(payload: EmailOTPRequest):
    return userRegistrationService.resend_email_otp(payload)

@registration.post("/send-mobile-otp")
async def send_mobile_otp(payload: MobileOTPRequest):
    return userRegistrationService.send_mobile_otp(payload)
    
@registration.post("/verify-mobile-otp")
async def verify_mobile_otp(payload: VerifyMobileOTPRequest):
    return userRegistrationService.verify_mobile_otp(payload)

@registration.post("/resend-mobile-otp")
async def resend_mobile_otp(payload: MobileOTPRequest):
    return userRegistrationService.resend_mobile_otp(payload)

@registration.post("/postuser")
async def post_user(user: User):
    return userRegistrationService.post_user(user)
