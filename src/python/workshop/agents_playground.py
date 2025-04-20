from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str="eastus2.api.azureml.ms;d50e14ba-0cb9-4dfe-ba3d-b25277ef2b6b;rg-agent-workshop-east_us;ecommerce-2141")

agent = project_client.agents.get_agent("asst_fkgPLAwkt32Dpfkc0D4iMK5C")

thread = project_client.agents.get_thread("thread_hrPOVXjZL4NixoYozBKWB41k")

message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="que tipo de tiendas vende contoso?"
)

# run = project_client.agents.create_and_process_run(
#     thread_id=thread.id,
#     assistant_id=agent.id)

# Corrected: Added the missing 'agent_id' argument
run = project_client.agents.create_and_process_run(
    thread_id=thread.id,
    # assistant_id=agent.id,
    agent_id=agent.id  # Assuming 'agent.id' is the correct value for 'agent_id'
)

messages = project_client.agents.list_messages(thread_id=thread.id)

for text_message in messages.text_messages:
    print(text_message.as_dict())

# Corrected iteration over messages
# for message in messages:
#     print(message.as_dict())