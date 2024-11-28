import time


class User:
    """
    Класс, содержащий информацию о пользователях: логин, пароль, возраст
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname


class Video:
    """
    Класс, содержащий информацию о видео: заголовок, время воспроизведения, секунда остановки
    (по умолчанию 0), ограничение по возрасту (по умолчанию отсутствует)
    """

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if (login, hash(password)) == user.get_info():
                self.current_user = user
                return user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует!')

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, find_word):
        video_list = []
        for video in self.videos:
            if find_word.lower() in str(video).lower():
                video_list.append(video)
        return video_list

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18, покиньте, пожалуйста, страницу!')
                    break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('Vasya_Pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('Urban_pithonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('Vasya_Pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')