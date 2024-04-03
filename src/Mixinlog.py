class Mixinlog:

    """
    Миксин-класс для отладочного отображения, которые будет
    наследоваться базовым классом Product и по наследству передаваться в другие
    """
    def __repr__(self):

        val = []
        for i in self.__dict__.values():
            val.append(i)
        return f'{self.__class__.__name__}{val}'