def is_lesson_in_course(les, lessons_list):
    if les in lessons_list:
        return True
    return False


def is_exercise_in_course(exercise, lessons_list):



lessons = input(). split(", ")

while True:
    command = input()

    if command == "course start":
        break

    command_as_list = command.split(":")
    action = command_as_list[0]
    lesson_tittle = command_as_list[1]

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

    elif action == "Swap":
        lesson_tittle2 = command_as_list[2]
        first_index = lessons.index(lesson_tittle)
        second_index = lessons.index(lesson_tittle2)

        if is_lesson_in_course(lesson_tittle, lessons) and is_lesson_in_course(lesson_tittle2, lessons):
            lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]

    elif action == "Exercise":
        index_lesson_for_exercise = lessons.index(lesson_tittle)
        if is_lesson_in_course(lesson_tittle, lessons) and not is_exercise_in_course():

            lessons.insert(index_lesson_for_exercise + 1, )

print(lessons)
