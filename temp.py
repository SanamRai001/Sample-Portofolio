import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('portofolio.db')
cursor = conn.cursor()

# SQL query to insert the article
sql = """
INSERT INTO posts (title, tags, author, date, content, created_at, updated_at)
VALUES (
    'Mastering ChatGPT Commands for Efficient Conversations',
    'AI, ChatGPT, Commands',
    'Sanam',
    '2024-07-31',
    '# Mastering ChatGPT Commands for Efficient Conversations\n\nIn the digital age, where communication is key, optimizing interactions with AI tools like ChatGPT can significantly enhance productivity and clarity. This article will delve into the specifics of various ChatGPT commands that can streamline your conversations, making them more efficient and effective.\n\n## Key Commands and Their Usage\n\n1. **#write_memory**\nThis command is crucial for storing information. By typing `#write_memory`, followed by the details you want to remember, you can ensure that important information is retained for future reference.\n\nExample:\n```\n#write_memory: Remember that my preferred programming language is Python.\n```\n\n2. **#recall_memory**\nWhen you need to retrieve stored information, use the `#recall_memory` command. This will bring up relevant details from past conversations.\n\nExample:\n```\n#recall_memory: What is my preferred programming language?\n```\n\n3. **#summarize**\nThe `#summarize` command is perfect for getting a brief overview of the current conversation or a specific topic. It condenses lengthy discussions into concise summaries.\n\nExample:\n```\n#summarize: Provide a summary of our conversation about cybersecurity.\n```\n\n4. **#give_advice**\nFor suggestions, opinions, or advice, the `#give_advice` command is invaluable. It provides tailored responses based on the context of your conversation.\n\nExample:\n```\n#give_advice: What are some good practices for web development?\n```\n\n5. **#current_task**\nTo keep track of the ongoing task or goal, use the `#current_task` command. It restates the current objective and provides relevant details or instructions.\n\nExample:\n```\n#current_task: What are we working on right now?\n```\n\n6. **#short_answer**\nWhen you need a brief and concise response, the `#short_answer` command is your go-to option.\n\nExample:\n```\n#short_answer: What is 2 + 2?\n```\n\n7. **#long_answer**\nFor detailed and thorough responses, the `#long_answer` command is ideal. It expands on topics, providing in-depth information.\n\nExample:\n```\n#long_answer: Explain the process of web development from start to finish.\n```\n\n## Conclusion\n\nMastering these ChatGPT commands can transform your interactions, making them more productive and efficient. By incorporating these commands into your daily routine, you can enhance your communication skills and make the most out of your AI assistant.',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
"""

# Execute the query
cursor.execute(sql)
conn.commit()

# Close the connection
conn.close()
