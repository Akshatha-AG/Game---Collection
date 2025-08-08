const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const grid = 20;
let count = 0;
let snake = [{ x: 160, y: 160 }];
let apple = { x: 320, y: 320 };
let dx = grid;
let dy = 0;
let score = 0;

function gameLoop() {
  requestAnimationFrame(gameLoop);

  if (++count < 8) return; // Speed
  count = 0;

  const head = { x: snake[0].x + dx, y: snake[0].y + dy };

  // End game if snake hits wall
  if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {
    alert("Game Over! Score: " + score);
    document.location.reload();
    return;
  }

  // End game if snake hits itself
  for (let segment of snake) {
    if (head.x === segment.x && head.y === segment.y) {
      alert("Game Over! Score: " + score);
      document.location.reload();
      return;
    }
  }

  snake.unshift(head);

  // Check apple collision
  if (head.x === apple.x && head.y === apple.y) {
    score++;
    apple.x = Math.floor(Math.random() * 20) * grid;
    apple.y = Math.floor(Math.random() * 20) * grid;
  } else {
    snake.pop();
  }

  // Draw background
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw snake
  ctx.fillStyle = "#00ff00";
  for (let segment of snake) {
    ctx.fillRect(segment.x, segment.y, grid - 1, grid - 1);
  }

  // Draw apple
  ctx.fillStyle = "red";
  ctx.fillRect(apple.x, apple.y, grid - 1, grid - 1);
}

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft" && dx === 0) {
    dx = -grid; dy = 0;
  } else if (e.key === "ArrowUp" && dy === 0) {
    dy = -grid; dx = 0;
  } else if (e.key === "ArrowRight" && dx === 0) {
    dx = grid; dy = 0;
  } else if (e.key === "ArrowDown" && dy === 0) {
    dy = grid; dx = 0;
  }
});

requestAnimationFrame(gameLoop);
