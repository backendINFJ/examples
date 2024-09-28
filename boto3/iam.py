import boto3

# MFA 프로필을 사용하는 세션 생성
session = boto3.Session(profile_name='mfa')

# IAM 클라이언트 생성
iam = session.client('iam')

# IAM 사용자 생성
response = iam.create_user(
    UserName='new-iam-user'  # 생성할 사용자의 이름
)

# 생성된 사용자의 정보 출력
print(f"IAM 사용자 생성 완료: {response['User']['UserName']}")