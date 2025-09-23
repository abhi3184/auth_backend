import time
from fastapi import HTTPException
from schemas.index import (
    EmailOTPRequest, EmailOTPVerifyRequest, 
    MobileOTPRequest, VerifyMobileOTPRequest, 
    UpdatePasswordReq
)
from repository.index import OTPRepository, ForgotPassRepository


class ForgotPasswordService:
    @staticmethod
    def send_email_otp(payload: EmailOTPRequest):
        user = ForgotPassRepository.get_user_by_email(payload.email)
        if not user:
            return {"success": False, "message": "Email ID not found"}
        try:
            return OTPRepository.send_email_otp(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send email OTP: {str(e)}")

    @staticmethod
    def verify_email_otp(payload: EmailOTPVerifyRequest):
        record = OTPRepository.otp_store.get(payload.email)
        if not record:
            return {"success": False, "message": "OTP not sent for this email"}

        if time.time() > record["expires_at"]:
            del OTPRepository.otp_store[payload.email]
            return {"success": False, "message": "Email OTP expired"}

        if payload.otp == record["otp"]:
            return {"success": True, "message": "OTP verified successfully"}
        return {"success": False, "message": "Invalid Email OTP"}

    @staticmethod
    def resend_email_otp(payload: EmailOTPRequest):
        try:
            return OTPRepository.send_email_otp(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to resend email OTP: {str(e)}")

    @staticmethod
    def send_mobile_otp(payload: MobileOTPRequest):
        user = ForgotPassRepository.get_user_by_mobile(payload.mobile)
        if not user:
            return {"success": False, "message": "Mobile number not found"}
        try:
            return OTPRepository.send_mobile_otp(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send mobile OTP: {str(e)}")

    @staticmethod
    def resend_mobile_otp(payload: MobileOTPRequest):
        return ForgotPasswordService.send_mobile_otp(payload)

    @staticmethod
    def verify_mobile_otp(payload: VerifyMobileOTPRequest):
        record = OTPRepository.mobile_otp_store.get(payload.mobile)
        if not record:
            return {"success": False, "message": "OTP not sent for this mobile"}

        if time.time() > record["expires_at"]:
            del OTPRepository.mobile_otp_store[payload.mobile]
            return {"success": False, "message": "Mobile OTP expired"}

        if payload.otp == record["otp"]:
            return {"success": True, "message": "OTP verified successfully"}
        return {"success": False, "message": "Invalid Mobile OTP"}

    @staticmethod
    def update_password(req: UpdatePasswordReq):
        user = ForgotPassRepository.get_user_by_email(req.email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return ForgotPassRepository.update_password(req.email, req.password)
