from memory_schemas import Conversation, UserPreferences, Milestone

conv = Conversation(
    user_id="student1",
    turn_id=1,
    role="user",
    content="I want help with calculus"
)

print(conv)


pref = UserPreferences(
    user_id="student1",
    preferences={"favorite_subjects": ["Math", "AI"]}
)

print(pref)


mile = Milestone(
    user_id="student1",
    milestone_id="ml1",
    description="Finish Linear Algebra course",
    status="planned"
)

print(mile)