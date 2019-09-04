class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0
    def __repr__(self):
        return f'<User {self.name}>'


def email_engaged_users(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function')
    else:
        if user.score > 500:
            send_engagement_notification(user.name)


def perform_calculation(metrics):
    return  metrics['clicks']*5 + metrics['hits']*2


def send_engagement_notification(user):
    print(f'Notification sent to {user}')


my_user = User('Nawab',{'clicks':61,'hits':100})
email_engaged_users(my_user)

print(perform_calculation(my_user.engagement_metrics))

# ----------------------------------------------------------------------------
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
        return 0
    finally:
        n_square = n ** 2
        return n_square

print(power_of_two())

