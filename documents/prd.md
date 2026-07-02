FluentFlow AI (working title)

An AI-powered English conversation practice platform where users improve conversational English through topic-based and scenario-based text conversations, receiving real-time corrections, optimized responses, vocabulary expansion, and personalized learning memory.

1. Vision

Most English learners know grammar and vocabulary but cannot hold a natural conversation.

The goal of FluentFlow AI is to simulate realistic conversations with an AI partner that:

Starts conversations naturally
Keeps conversations flowing
Corrects mistakes
Teaches vocabulary in context
Tracks learning progress
Creates custom roleplay scenarios
Builds long-term conversational fluency

The experience should feel like:

ChatGPT
+
Duolingo
+
Speak
+
Roleplay Simulator
+
Vocabulary Trainer
2. Problem Statement

Current English learning apps have major problems:

Duolingo
Good for vocabulary
Bad for real conversation
Grammar Apps
Teach rules
Don't build speaking confidence
ChatGPT
Good conversation
No structured learning
No vocabulary tracking
No progress system
Language Exchange Apps
Need another human
Availability issues

FluentFlow solves this by providing:

Unlimited conversation practice
+
Real-time correction
+
Vocabulary learning
+
Scenario simulation
+
Personalized memory
3. Core User Personas
Persona 1

Student

Goal:

Improve spoken English
Prepare for interviews
Persona 2

Working Professional

Goal:

Business communication
Meeting discussions
Client conversations
Persona 3

Beginner Learner

Goal:

Build confidence
Speak without fear
4. Core Features
Feature 1
Topic-Based Conversations

Database contains:

50-100 topics

Examples:

Travel
Movies
Technology
Sports
Food
Education
Business
Friendship
Career
Health
AI
Startups

When user opens app:

Suggested Topics

Card Layout:

Travel
Technology
Movies
Food
Career
Custom Scenario

User selects:

Travel

AI starts:

Have you ever traveled outside your city?

Conversation begins.

Feature 2
Scenario-Based Conversations

User creates scenario.

Example:

I am attending a job interview.
You are HR.

AI creates session.

Example:

Welcome, tell me about yourself.

Conversation continues.

Scenario Templates

Examples:

Job Interview

Coffee Shop

Airport

Hotel Check-In

Business Meeting

Customer Support

College Admission

Doctor Visit

Dating Conversation

Sales Pitch
Feature 3
Conversation Learning Loop

Every user message triggers:

Step 1

User Response

I go to beach last week.
Step 2

AI Correction

Correction:

I went to the beach last week.
Step 3

Natural Alternative

Better Version:

I visited the beach last week and had a great time.
Step 4

Vocabulary Teaching

Vocabulary:

Relaxing

Definition:

Helping you feel calm and stress-free.
Step 5

Five Examples

1. The beach was very relaxing.

2. Music can be relaxing.

3. I had a relaxing weekend.

4. Reading books is relaxing.

5. The vacation was relaxing.
Step 6

Continue Conversation

What activities did you enjoy at the beach?

This becomes the core loop.

Feature 4
Vocabulary Memory System

Most apps repeat words.

We don't want that.

Database:

user_vocab

Example:

Relaxing
Confidence
Opportunity
Challenge
Efficient

Before generating vocabulary:

AI checks:

Has user learned this before?

If yes:

Generate new vocabulary

Result:

No repeated words.

Feature 5
Difficulty Levels
Beginner

AI:

Short sentences
Simple vocabulary
Intermediate

AI:

Natural conversation
Moderate vocabulary
Advanced

AI:

Complex discussions
Idioms
Professional communication
Feature 6
Progress Dashboard

Track:

Total Conversations
127
Vocabulary Learned
842 words
Topics Completed
39/50
Grammar Corrections
1452
Streak
25 days
Feature 7
Conversation Switch

User can change conversation anytime.

Example:

Travel
→
Job Interview

Previous conversation saved.

New conversation starts.

5. AI Architecture
Conversation Engine

Prompt Structure:

You are an English tutor.

Scenario:
Travel Discussion

Student Level:
Intermediate

Previous Vocabulary:
[list]

Rules:

1. Continue conversation naturally.
2. Correct mistakes.
3. Give optimized response.
4. Introduce ONE new vocabulary.
5. Provide FIVE examples.
6. Never repeat vocabulary.
7. Keep conversation engaging.
6. Multi-Groq API Rotation

Since Groq Free Tier has limits.

Create:

GROQ_KEYS = [
   key1,
   key2,
   key3,
   key4,
   key5
]

Request flow:

Try Key 1
 ↓
Rate Limited?
 ↓
Try Key 2
 ↓
Rate Limited?
 ↓
Try Key 3

Implementation:

for key in GROQ_KEYS:
    try:
        response = call_groq(key)
        return response
    except RateLimitError:
        continue
7. Recommended Tech Stack

Frontend:

Next.js
Tailwind
Shadcn UI

Backend:

FastAPI

Database:

PostgreSQL

ORM:

SQLAlchemy

Authentication:

Better Auth

Deployment:

Vercel
+
Railway

AI:

Groq
8. Database Design
Users
users
Topics
topics
id
title
description
difficulty
Conversations
conversations
id
user_id
topic_id
scenario_id
created_at
Messages
messages
id
conversation_id
role
content
created_at
Vocabulary
vocabulary
id
word
definition
User Vocabulary
user_vocabulary
id
user_id
word_id
learned_at
9. UI / UX Design
Dashboard
+----------------------------------+
| Good Evening Sanjay             |
+----------------------------------+

Continue Learning

[ Travel Topic ]

Suggested Topics

[ Travel ]
[ Movies ]
[ Technology ]
[ Business ]
[ AI ]

Create Scenario

+-------------------------+
| Describe Scenario       |
+-------------------------+

[ Create ]
Chat Screen
--------------------------------

AI Message

Correction
Optimized Response

Vocabulary:
Opportunity

Definition

5 Example Sentences

--------------------------------

Your Reply

[ Type here ]

[ Send ]

--------------------------------