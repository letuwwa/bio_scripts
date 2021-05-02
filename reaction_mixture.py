class ReactionMixture:
    def __init__(self):
        self.reaction_mixture_volume = self.reaction_mixture_volume_input()
        self.mix2x_volume = self.reaction_mixture_volume / 2

    def result_print(self):
        pass

    @classmethod
    def _error_pause(cls):
        print('Некорректный ввод! Попробуйте еще раз...')
        input()

    @classmethod
    def reaction_mixture_volume_input(cls):
        while True:
            try:
                water_volume = float(input('Введите объем реакционной смеси (в микролитрах): '))
                if water_volume > 0:
                    return water_volume
                else:
                    cls._error_pause()
            except ValueError:
                cls._error_pause()


if __name__ == "__main__":
    ReactionMixture()
