from gym.envs.registration import register

register(
    id='boring_conversation-v0',
    entry_point='gym_boring_conversation.envs:boring_conversationEnv',
)
register(
    id='boring_conversation-extrahard-v0',
    entry_point='gym_boring_conversation.envs:boring_conversationExtraHardEnv',
)