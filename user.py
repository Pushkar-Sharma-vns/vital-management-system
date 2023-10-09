from utility import convert_string_to_datetime, get_vitals_for_username


class CreateUser:
    # user_list = []
    validated_username = set()
    
    def __init__(self, username, age, gender, medical_condition=None):
        self.username = username
        self.age = age
        self.gender = gender
        self.medical_condition = medical_condition
        
    def create(self, user_list):
        self.validate_username()
        user = {}
        user["username"] = self.username
        user["age"] = self.age
        user["gender"] = self.gender
        if self.medical_condition:
            user["medical_condition"] = self.medical_condition
        user_list.append(user)
        # print(str(user_list))
        return {"status": "success", "message": f"User {self.username} created."}
        
    def validate_username(self):
        try:
            self.validated_username.add(self.username)
        except Exception as e:
            print("Username already present, try creating user using different username!")
            