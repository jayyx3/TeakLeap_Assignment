Candidate Management API
🎯Problem Statement
Build a simple backend API to manage candidates for a recruitment system.
You need to implement a small service where:
• Recruiters can add candidates
• View a list of candidates
• Update candidate status
⚙️Requirements
Use:
Language: Python
Framework: FastAPI
📦Features to Implement

1. Create Candidate
POST /candidates
Request body:
{
"name": "John Doe",
"email": "john@example.com",
"skill": "Python",
"status": "applied"
}
Validation:
email must be valid
status should be one of: applied, interview, selected, rejected

2. Get All Candidates
GET /candidates

Return list of all candidates
Optional: support filtering by status (query param)
Example:
GET /candidates?status=interview

3. Update Candidate Status

PUT /candidates/{id}/status
Request:
{
"status": "interview"
}

Expectations:
We are expecting you to use AI IDE such as Copilot to solve this problem.
