def is_lesson_in_course(les, lessons_list):
    if les in lessons_list:
        return True
    return False


def is_exercise_in_course(exerc, lessons_list):
    if exerc in lessons_list:
        return True
    return False


lessons = input(). split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command_as_list = command.split(":")
    action = command_as_list[0]
    lesson_tittle = command_as_list[1]
    exercise = f"{lesson_tittle}-Exercise"

    if action == "Add":
        if not is_lesson_in_course(lesson_tittle, lessons):
            lessons.append(lesson_tittle)

    elif action == "Insert":
        index_to_insert = int(command_as_list[2])
        if not is_lesson_in_course(lesson_tittle, lessons):
            lessons.insert(index_to_insert, lesson_tittle)

    elif action == "Remove":
        if is_lesson_in_course(lesson_tittle, lessons):
            lessons.remove(lesson_tittle)
            if is_exercise_in_course(exercise, lessons):
                lessons.remove(exercise)

    elif action == "Swap":
        lesson_tittle2 = command_as_list[2]
        exercise2 = f"{lesson_tittle2}-Exercise"
        first_index = lessons.index(lesson_tittle)
        second_index = lessons.index(lesson_tittle2)

        if is_lesson_in_course(lesson_tittle, lessons) and is_lesson_in_course(lesson_tittle2, lessons):
            lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
            if is_exercise_in_course(exercise, lessons):
                lessons.remove(exercise)
                lessons.insert(second_index + 1, exercise)

            if is_exercise_in_course(exercise2, lessons):
                lessons.remove(exercise2)
                lessons.insert(first_index + 1, exercise2)

    elif action == "Exercise":
        if not is_lesson_in_course(lesson_tittle, lessons):
            lessons.append(lesson_tittle)
            lessons.append(exercise)
        else:
            index_lesson_for_exercise = lessons.index(lesson_tittle)
            if is_lesson_in_course(lesson_tittle, lessons) and not is_exercise_in_course(exercise, lessons):
                lessons.insert(index_lesson_for_exercise + 1, exercise)

for lesson in lessons:
    print(f"{lessons.index(lesson) + 1}.{lesson}")
