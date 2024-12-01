<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chào mừng đến với web của Quảng Thiên</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f7f7f7;
            color: #333;
            padding: 50px;
        }
        h1 {
            color: #ff5733;
        }
        h2 {
            color: #4CAF50;
        }
        .question {
            font-size: 24px;
            margin-top: 20px;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            margin: 10px;
            background-color: #ff5733;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #d84b2a;
        }
        .answer {
            font-size: 20px;
            color: #007bff;
            font-weight: bold;
            display: none;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1>Chào mừng đến với web của Quảng Thiên</h1>
    <h2>Vui lòng trả lời câu hỏi dưới đây:</h2>
    
    <div class="question">
        Bạn có phải là con chó không?
    </div>

    <div>
        <button onclick="showAnswer('a')">a. Dog</button>
        <button onclick="showAnswer('b')">b. Cún</button>
        <button onclick="showAnswer('c')">c. Cờ hó</button>
        <button onclick="showAnswer('d')">d. Bạn là chó</button>
    </div>

    <p id="answerA" class="answer">Bạn chọn: Dog. Câu trả lời không đúng!</p>
    <p id="answerB" class="answer">Bạn chọn: Cún. Câu trả lời không đúng!</p>
    <p id="answerC" class="answer">Bạn chọn: Cờ hó. Câu trả lời không đúng!</p>
    <p id="answerD" class="answer">Chúc mừng! Bạn chọn đúng! Bạn là chó!</p>

    <script>
        function showAnswer(answer) {
            // Ẩn tất cả các câu trả lời
            document.getElementById('answerA').style.display = 'none';
            document.getElementById('answerB').style.display = 'none';
            document.getElementById('answerC').style.display = 'none';
            document.getElementById('answerD').style.display = 'none';

            // Hiển thị câu trả lời tương ứng
            if (answer === 'a') {
                document.getElementById('answerA').style.display = 'block';
            } else if (answer === 'b') {
                document.getElementById('answerB').style.display = 'block';
            } else if (answer === 'c') {
                document.getElementById('answerC').style.display = 'block';
            } else if (answer === 'd') {
                document.getElementById('answerD').style.display = 'block';
            }
        }
    </script>
</body>
</html>
