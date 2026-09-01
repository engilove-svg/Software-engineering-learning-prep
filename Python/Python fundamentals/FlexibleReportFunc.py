def generate_report(**kwargs):
    for key in kwargs:
        print(key,":",kwargs[key])

generate_report(
    name="Loveleen",
    age=23,
    course="CSE",
    skills="Python",
    city="Sault Ste. Marie"
)