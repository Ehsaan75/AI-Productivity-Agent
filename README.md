# AI Productivity Agent

A powerful command-line AI assistant that combines task management with intelligent insights using OpenAI's GPT models. Perfect for developers, students, and anyone looking to boost their productivity with AI-powered task prioritization and guidance.

##  Features

### Core Functionality
- **🤖 AI-Powered Assistance**: Ask questions and get intelligent responses using GPT-3.5-turbo
- ** Task Management**: Full CRUD operations for your to-do list
- **🎯 Smart Prioritization**: Get AI-generated summaries and priority suggestions for your tasks
- ** Persistent Storage**: Tasks are saved to `todo.json` and persist between sessions

### Available Commands
- **`ask`** - Ask general knowledge questions or get productivity advice
- **`add`** - Add new tasks to your to-do list
- **`view`** - Display all current tasks with their status
- **`complete`** - Mark tasks as completed
- **`delete`** - Remove tasks from your list
- **`summarise`** - Get AI-powered workload analysis and priority recommendations

## 🛠️ Setup

### Prerequisites
- Python 3.7 or higher
- OpenAI API key (get one at [platform.openai.com](https://platform.openai.com))

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-bootcamp
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install openai python-dotenv
   ```

4. **Set up environment variables**
   
   Create a `.env` file in your project root:
   ```bash
   echo OPENAI_API_KEY=sk-your_actual_api_key_here > .env
   ```
   
   **⚠️ Important**: Replace `sk-your_actual_api_key_here` with your real OpenAI API key

## 📖 Usage Examples

### Basic Task Management
```bash
# Add tasks
python main.py add "Learn Python basics"
python main.py add "Build a machine learning project"
python main.py add "Review code documentation"

# View your tasks
python main.py view

# Mark a task as complete
python main.py complete 1

# Delete a task
python main.py delete 2

# Get AI-powered summary and priorities
python main.py summarise
```

### AI Assistance
```bash
# Ask productivity questions
python main.py ask "What are three tips for staying focused while coding?"

# Get learning advice
python main.py ask "How should I approach learning machine learning as a beginner?"

# Request time management tips
python main.py ask "Explain the Pomodoro technique for time management"
```

### Interactive Testing
```bash
# Run comprehensive tests
python agent.py
```

##  Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

### File Structure
```
ai-bootcamp/
├── agent.py          # Core agent class with all functionality
├── main.py           # Command-line interface
├── todo.json         # Task storage (auto-created)
├── .env              # Environment variables (create this)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

##  Testing

Test each functionality individually:
```bash
# Test task operations
python main.py add "Test task"
python main.py view
python main.py complete 1
python main.py delete 1

# Test AI functionality
python main.py ask "What is 2+2?"
```

## 🚨 Troubleshooting

### Common Issues

1. **"No module named 'openai'"**
   - Make sure your virtual environment is activated
   - Run: `pip install openai python-dotenv`

2. **"API key not found"**
   - Check that your `.env` file exists and contains the correct API key
   - Ensure the `.env` file is in your project root directory

3. **"Cannot import name 'OPENAI'"**
   - The correct import is `from openai import OpenAI` (capitalized)

4. **Tasks not saving**
   - Check file permissions in your project directory
   - Ensure `todo.json` is writable

### Debug Mode
Run with verbose output to see what's happening:
```bash
python -v main.py view
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- OpenAI for providing the GPT API
- The Python community for excellent libraries
- Contributors and users of this project

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Happy coding and stay productive! 🚀**