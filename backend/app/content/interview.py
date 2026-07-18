"""
Job Interview Topic Content

This file contains all content related to the Job Interview topic.
No Django models should be imported here.

The seed_data management command will import this file
and populate the database.
"""

INTERVIEW = {
    "topic": {
        "title": "Job Interview",
        "description": "Practice English for job interviews, introducing yourself, discussing experience, answering interview questions, and communicating professionally.",
        "category": "Career",
        "difficulty": "B1",
        "grammar_focus": "Present Perfect",
        "vocabulary_focus": "Career & Professional Communication",
        "estimated_turns": 45,
        "icon": "💼",
        "display_order": 4,
        "is_active": True,
    },

    # "learning_objectives": [
    #     "Introduce yourself professionally",
    #     "Describe your work experience",
    #     "Answer interview questions confidently",
    # ],

    "scenarios": [
        {
            "title": "Self Introduction",
            "description": "Introduce yourself to the interviewer.",
            "ai_role": "Interviewer",
            "user_role": "Job Candidate",
            "opening_prompt": "Good morning! Thank you for coming today. Could you please introduce yourself?",
            "learning_objective": "Give a professional self-introduction.",
            "difficulty": "B1",
            "grammar_focus": "Present Perfect",
            "vocabulary_focus": "Self Introduction",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Work Experience",
            "description": "Talk about previous jobs and responsibilities.",
            "ai_role": "Hiring Manager",
            "user_role": "Job Candidate",
            "opening_prompt": "Can you tell me about your previous work experience?",
            "learning_objective": "Describe previous experience clearly.",
            "difficulty": "B1",
            "grammar_focus": "Present Perfect",
            "vocabulary_focus": "Work Experience",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Technical Interview",
            "description": "Answer technical and problem-solving questions.",
            "ai_role": "Technical Interviewer",
            "user_role": "Candidate",
            "opening_prompt": "Let's discuss some technical questions related to your skills.",
            "learning_objective": "Explain technical knowledge confidently.",
            "difficulty": "B1",
            "grammar_focus": "Present Perfect",
            "vocabulary_focus": "Technical Skills",
            "max_turns": 45,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Strengths and Weaknesses",
            "description": "Discuss your personal strengths and areas for improvement.",
            "ai_role": "HR Manager",
            "user_role": "Candidate",
            "opening_prompt": "What would you say are your biggest strengths and weaknesses?",
            "learning_objective": "Talk about personal qualities professionally.",
            "difficulty": "B1",
            "grammar_focus": "Present Perfect",
            "vocabulary_focus": "Professional Skills",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Salary Discussion",
            "description": "Discuss salary expectations and benefits professionally.",
            "ai_role": "HR Manager",
            "user_role": "Candidate",
            "opening_prompt": "Let's discuss your salary expectations for this role.",
            "learning_objective": "Negotiate professionally.",
            "difficulty": "B2",
            "grammar_focus": "Present Perfect",
            "vocabulary_focus": "Salary Negotiation",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
    ],

    "vocabulary": [
    {
      "word": "resume",
      "definition": "A document describing your education, skills, and work experience.",
      "difficulty": "A2"
    },
    {
      "word": "interview",
      "definition": "A meeting where an employer evaluates a job candidate.",
      "difficulty": "A2"
    },
    {
      "word": "experience",
      "definition": "Knowledge or skills gained through work or activities.",
      "difficulty": "A2"
    },
    {
      "word": "qualification",
      "definition": "A skill, achievement, or certification that makes someone suitable for a job.",
      "difficulty": "B1"
    },
    {
      "word": "skills",
      "definition": "Abilities developed through learning or experience.",
      "difficulty": "A2"
    },
    {
      "word": "strength",
      "definition": "A quality or ability that you do well.",
      "difficulty": "A2"
    },
    {
      "word": "weakness",
      "definition": "An area where improvement is needed.",
      "difficulty": "A2"
    },
    {
      "word": "teamwork",
      "definition": "Working effectively with other people.",
      "difficulty": "A2"
    },
    {
      "word": "leadership",
      "definition": "The ability to guide and motivate others.",
      "difficulty": "B1"
    },
    {
      "word": "communication",
      "definition": "The ability to exchange information clearly.",
      "difficulty": "A2"
    },
    {
      "word": "responsibility",
      "definition": "A task or duty that you are expected to complete.",
      "difficulty": "B1"
    },
    {
      "word": "project",
      "definition": "A planned piece of work with a specific goal.",
      "difficulty": "A2"
    },
    {
      "word": "deadline",
      "definition": "The date by which work must be completed.",
      "difficulty": "B1"
    },
    {
      "word": "promotion",
      "definition": "Advancement to a higher job position.",
      "difficulty": "B1"
    },
    {
      "word": "salary",
      "definition": "The money paid regularly for doing a job.",
      "difficulty": "A2"
    },
    {
      "word": "company",
      "definition": "A business organization.",
      "difficulty": "A1"
    },
    {
      "word": "manager",
      "definition": "A person responsible for supervising employees.",
      "difficulty": "A2"
    },
    {
      "word": "candidate",
      "definition": "A person applying for a job.",
      "difficulty": "A2"
    },
    {
      "word": "employee",
      "definition": "A person who works for a company.",
      "difficulty": "A1"
    },
    {
      "word": "employer",
      "definition": "A person or company that hires employees.",
      "difficulty": "A2"
    },
    {
      "word": "job",
      "definition": "Regular paid work.",
      "difficulty": "A1"
    },
    {
      "word": "career",
      "definition": "The long-term profession or occupation of a person.",
      "difficulty": "B1"
    },
    {
      "word": "profession",
      "definition": "A type of skilled job.",
      "difficulty": "B1"
    },
    {
      "word": "position",
      "definition": "A particular job in an organization.",
      "difficulty": "A2"
    },
    {
      "word": "role",
      "definition": "The function or job performed by a person.",
      "difficulty": "A2"
    },
    {
      "word": "department",
      "definition": "A division within a company.",
      "difficulty": "B1"
    },
    {
      "word": "organization",
      "definition": "A company or institution with a particular purpose.",
      "difficulty": "B1"
    },
    {
      "word": "interviewer",
      "definition": "The person who asks questions during an interview.",
      "difficulty": "A2"
    },
    {
      "word": "hiring manager",
      "definition": "The manager responsible for selecting new employees.",
      "difficulty": "B1"
    },
    {
      "word": "human resources",
      "definition": "The department responsible for employee management.",
      "difficulty": "B1"
    },
    {
      "word": "application",
      "definition": "A formal request for a job.",
      "difficulty": "A2"
    },
    {
      "word": "cover letter",
      "definition": "A letter sent with a resume when applying for a job.",
      "difficulty": "B1"
    },
    {
      "word": "portfolio",
      "definition": "A collection of work samples.",
      "difficulty": "B1"
    },
    {
      "word": "achievement",
      "definition": "Something accomplished successfully.",
      "difficulty": "B1"
    },
    {
      "word": "accomplishment",
      "definition": "A successful result gained through effort.",
      "difficulty": "B1"
    },
    {
      "word": "goal",
      "definition": "Something you want to achieve.",
      "difficulty": "A2"
    },
    {
      "word": "objective",
      "definition": "A specific aim or target.",
      "difficulty": "B1"
    },
    {
      "word": "career growth",
      "definition": "Progress and advancement in a career.",
      "difficulty": "B1"
    },
    {
      "word": "professional",
      "definition": "Showing skill and appropriate workplace behavior.",
      "difficulty": "A2"
    },
    {
      "word": "confidence",
      "definition": "Belief in your abilities.",
      "difficulty": "B1"
    },
    {
      "word": "motivation",
      "definition": "The reason for working toward a goal.",
      "difficulty": "B1"
    },
    {
      "word": "enthusiasm",
      "definition": "Strong interest and excitement.",
      "difficulty": "B1"
    },
    {
      "word": "adaptability",
      "definition": "The ability to adjust to new situations.",
      "difficulty": "B1"
    },
    {
      "word": "flexibility",
      "definition": "The willingness to adapt to change.",
      "difficulty": "B1"
    },
    {
      "word": "problem-solving",
      "definition": "The ability to find solutions to problems.",
      "difficulty": "B1"
    },
    {
      "word": "decision-making",
      "definition": "The process of choosing the best option.",
      "difficulty": "B1"
    },
    {
      "word": "critical thinking",
      "definition": "Careful analysis to make good decisions.",
      "difficulty": "B2"
    },
    {
      "word": "initiative",
      "definition": "The ability to act independently.",
      "difficulty": "B1"
    },
    {
      "word": "creativity",
      "definition": "The ability to produce new ideas.",
      "difficulty": "B1"
    },
    {
      "word": "productivity",
      "definition": "The amount of useful work completed.",
      "difficulty": "B1"
    },
    {
      "word": "performance",
      "definition": "How well someone does their job.",
      "difficulty": "B1"
    },
    {
      "word": "task",
      "definition": "A piece of work assigned to someone.",
      "difficulty": "A2"
    },
    {
      "word": "duty",
      "definition": "Something you are expected to do.",
      "difficulty": "A2"
    },
    {
      "word": "supervisor",
      "definition": "A person who oversees employees.",
      "difficulty": "B1"
    },
    {
      "word": "colleague",
      "definition": "A person you work with.",
      "difficulty": "A2"
    },
    {
      "word": "client",
      "definition": "A person or business receiving services.",
      "difficulty": "A2"
    },
    {
      "word": "meeting",
      "definition": "A gathering to discuss work.",
      "difficulty": "A2"
    },
    {
      "word": "presentation",
      "definition": "A formal talk given to an audience.",
      "difficulty": "B1"
    },
    {
      "word": "training",
      "definition": "Learning skills for a job.",
      "difficulty": "A2"
    },
    {
      "word": "certification",
      "definition": "An official document proving qualifications.",
      "difficulty": "B1"
    },
    {
      "word": "degree",
      "definition": "A university qualification.",
      "difficulty": "A2"
    },
    {
      "word": "education",
      "definition": "The process of learning and gaining knowledge.",
      "difficulty": "A2"
    },
    {
      "word": "reference",
      "definition": "A person who recommends a job applicant.",
      "difficulty": "B1"
    },
    {
      "word": "contract",
      "definition": "A legal employment agreement.",
      "difficulty": "B1"
    },
    {
      "word": "benefits",
      "definition": "Additional advantages provided with a job.",
      "difficulty": "B1"
    },
    {
      "word": "bonus",
      "definition": "Extra money paid in addition to salary.",
      "difficulty": "B1"
    },
    {
      "word": "compensation",
      "definition": "Salary and other financial rewards.",
      "difficulty": "B2"
    },
    {
      "word": "negotiation",
      "definition": "Discussion to reach an agreement.",
      "difficulty": "B2"
    },
    {
      "word": "expectation",
      "definition": "What someone believes or hopes will happen.",
      "difficulty": "B1"
    },
    {
      "word": "opportunity",
      "definition": "A favorable chance for progress.",
      "difficulty": "B1"
    },
    {
      "word": "challenge",
      "definition": "A difficult task requiring effort.",
      "difficulty": "B1"
    },
    {
      "word": "success",
      "definition": "The achievement of a desired goal.",
      "difficulty": "A2"
    },
    {
      "word": "failure",
      "definition": "The lack of success in achieving something.",
      "difficulty": "B1"
    },
    {
      "word": "improvement",
      "definition": "The process of becoming better.",
      "difficulty": "A2"
    },
    {
      "word": "technical skills",
      "definition": "Practical abilities related to a specific field.",
      "difficulty": "B1"
    },
    {
      "word": "software",
      "definition": "Computer programs used to perform tasks.",
      "difficulty": "A2"
    },
    {
      "word": "programming",
      "definition": "Writing computer code.",
      "difficulty": "B1"
    },
    {
      "word": "debugging",
      "definition": "Finding and fixing software errors.",
      "difficulty": "B1"
    },
    {
      "word": "solution",
      "definition": "An answer to a problem.",
      "difficulty": "A2"
    },
    {
      "word": "analysis",
      "definition": "Careful examination of information.",
      "difficulty": "B1"
    },
    {
      "word": "efficiency",
      "definition": "Completing work with little waste of time or effort.",
      "difficulty": "B1"
    },
    {
      "word": "time management",
      "definition": "The ability to use time effectively.",
      "difficulty": "B1"
    },
    {
      "word": "work ethic",
      "definition": "A commitment to working responsibly.",
      "difficulty": "B1"
    },
    {
      "word": "reliability",
      "definition": "The quality of being dependable.",
      "difficulty": "B1"
    },
    {
      "word": "punctuality",
      "definition": "The habit of being on time.",
      "difficulty": "B1"
    },
    {
      "word": "multitasking",
      "definition": "Handling more than one task at the same time.",
      "difficulty": "B1"
    },
    {
      "word": "work environment",
      "definition": "The conditions in which people work.",
      "difficulty": "B1"
    },
    {
      "word": "career objective",
      "definition": "A professional goal for future growth.",
      "difficulty": "B1"
    },
    {
      "word": "self-introduction",
      "definition": "A professional description of yourself.",
      "difficulty": "B1"
    },
    {
      "word": "professional development",
      "definition": "Improving skills and knowledge for a career.",
      "difficulty": "B2"
    },
    {
      "word": "work history",
      "definition": "A record of previous employment.",
      "difficulty": "B1"
    },
    {
      "word": "employment",
      "definition": "The state of having a paid job.",
      "difficulty": "A2"
    },
    {
      "word": "vacancy",
      "definition": "An available job position.",
      "difficulty": "B1"
    },
    {
      "word": "offer",
      "definition": "A proposal to hire a candidate.",
      "difficulty": "A2"
    },
    {
      "word": "onboarding",
      "definition": "The process of joining a new company.",
      "difficulty": "B2"
    }
  ]
}