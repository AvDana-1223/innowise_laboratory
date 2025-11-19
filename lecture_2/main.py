def main():
    current_age, user_name = greet_user()
    life_stage = generate_profile(current_age)
    hobbies = get_user_hobbies()

    user_profile = {
        'name': user_name,
        'age': current_age,
        'stage': life_stage,
        'hobbies': hobbies,

    }

    print("---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if not user_profile["hobbies"]:
        print("You didn't mention any hobbies")
    else:
        print(f"Favorite Hobbies ({len(user_profile["hobbies"])}):")

        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")

    print("---")


def greet_user():
    user_name = input("Hello! Enter your full name: ")

    birth_year_str = input('Enter your birth year: ')
    current_year = 2025
    birth_year = int(birth_year_str)

    current_age = current_year - birth_year

    return current_age, user_name


def generate_profile(age):
    if age in range(0, 13):
        return "Child"

    if age in range(13, 20):
        return 'Teenager'

    return 'Adult'


def get_user_hobbies():
    hobbies = []

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

        if hobby == "stop":
            break

        hobbies.append(hobby)

    return hobbies


if __name__ == "__main__":
    main()
