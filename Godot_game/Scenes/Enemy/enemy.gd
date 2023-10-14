@tool
extends StaticBody3D
class_name Enemy

signal bullet_collision
var go_left = true
var moving_range = 5
var act := ""
var counter = 0
var SPEED = 3

func _ready():
	bullet_collision.connect(Callable(self, "_on_bullet_collision"))

func _physics_process(delta):
	var movement = ["left", "right", "up", "down"]
	var force_run = false
	if not Engine.is_editor_hint():
		if self.position.z > moving_range:
			movement.erase("left")
			force_run = true
		if self.position.z < -moving_range:
			movement.erase("right")
			force_run = true
		if self.position.y < 0.5:
			movement.erase("down")
			force_run = true
		if self.position.y > 5:
			movement.erase("up")
			force_run = true
		if force_run or counter % 100 == 0:
			act = movement[randi() % movement.size()]
		if act == "left":
			self.position.z += SPEED * delta
		elif act == "right":
			self.position.z -= SPEED * delta
		elif act == "up":
			self.position.y += SPEED * delta
		else:
			self.position.y -= SPEED * delta
	counter += 1
	
func _on_bullet_collision():
	queue_free()

