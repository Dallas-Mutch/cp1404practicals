from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # java = ProgrammingLanguage("Java", "Static", False, 1995)
    # cplusplus = ProgrammingLanguage("C++", "Static", False, 1983)

    languages = [python, ruby, visual_basic]
    print(python)

    print("The dynamic typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == '__main__':
    main()
