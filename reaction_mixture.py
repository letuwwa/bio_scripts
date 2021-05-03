class ReactionMixture:
    def __init__(self):
        self.reaction_mixture_volume = self.reaction_mixture_volume_input()
        self.dnc_volume = 2.0
        self.mix2x_volume = self.reaction_mixture_volume / 2
        self.water_volume = self.reaction_mixture_volume - self.mix2x_volume - self.dnc_volume
        self.primers = self.reaction_mixture_volume * 6e-3
        self.result_print()

    def result_print(self):
        print("""
        \tОбъем реакционной жидкости: {}\n
        \tОбъем ДНК: {}
        \tОбъем Mix2X: {}
        \tОбъем воды: {}\n
        \tКонцентрация праймеров для введенного объема реакционной смеси составляет: {} пикомоль
        """.format(self.reaction_mixture_volume,
                   self.dnc_volume,
                   self.mix2x_volume,
                   self.water_volume,
                   self.primers))

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
