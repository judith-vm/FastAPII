from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")

def index():
    return "Ingresa /animacion en la barra"

@app.get("/animacion", response_class=HTMLResponse)
async def mostrar_aprender():
    html_content = """
    <html>
    <head>

        <title>Animacion</title>

    </head>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }

        canvas {
            border: 2px solid #000;
            background-color: #ddd;
            animation: heartbeat 1s infinite alternate; 
        }

        @keyframes heartbeat {
            from { transform: scale(1); }
            to { transform: scale(1.2); }
        }
    </style>
</head>
<body>
    <canvas id="textCanvas" width="250" height="250"></canvas>

    <script>
        const canvas = document.getElementById("textCanvas");
        const ctx = canvas.getContext("2d");

        function drawText() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const text = "UsandoFastAPI";
            const x = canvas.width - 220;
            const y = canvas.height / 2;

            ctx.font = "bold 24px Arial";
            ctx.fillStyle = "green";
            ctx.fillText(text, x, y);
        }

        drawText();
    </script>
</body>
</html>

    """
    return HTMLResponse(content=html_content, status_code=200)