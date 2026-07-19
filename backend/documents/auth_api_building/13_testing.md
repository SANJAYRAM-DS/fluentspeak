# Testing Guide

This document provides `curl` commands to manually test the API. 
To test, ensure the Django server is running: `python manage.py runserver`

## 1. Register
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "SecurePassword123!", "password_confirm": "SecurePassword123!", "first_name": "John", "last_name": "Doe"}'
```
*Expected: 201 Created with JSON containing tokens and user data.*

## 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "SecurePassword123!"}'
```
*Expected: 200 OK with `access` and `refresh` tokens.*

## 3. Get Current User (Protected)
*Replace `<YOUR_ACCESS_TOKEN>` with the token from Step 2.*
```bash
curl -X GET http://127.0.0.1:8000/api/auth/me \
-H "Authorization: Bearer <YOUR_ACCESS_TOKEN>"
```
*Expected: 200 OK with user and profile data.*

## 4. Refresh Token
*Replace `<YOUR_REFRESH_TOKEN>` with the token from Step 2.*
```bash
curl -X POST http://127.0.0.1:8000/api/auth/refresh \
-H "Content-Type: application/json" \
-d '{"refresh": "<YOUR_REFRESH_TOKEN>"}'
```
*Expected: 200 OK with new access and refresh tokens.*

## 5. Logout
```bash
curl -X POST http://127.0.0.1:8000/api/auth/logout \
-H "Authorization: Bearer <YOUR_ACCESS_TOKEN>"
```
*Expected: 200 OK with success message.*

## 6. Forgot Password
```bash
curl -X POST http://127.0.0.1:8000/api/auth/forgot-password \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com"}'
```
*Expected: 200 OK with the reset token in the message (for V1 testing).*

## 7. Reset Password
*Replace `<RESET_TOKEN>` with the token returned in Step 6.*
```bash
curl -X POST http://127.0.0.1:8000/api/auth/reset-password \
-H "Content-Type: application/json" \
-d '{"token": "<RESET_TOKEN>", "new_password": "NewPassword123!", "new_password_confirm": "NewPassword123!"}'
```
*Expected: 200 OK with success message.*
