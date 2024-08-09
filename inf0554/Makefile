run: compile blue yellow green

compile:
	go build -o demo src/main.go

blue:
	INF0554_PORT=:8080 INF0554_COLOR=blue ./demo &

yellow:
	INF0554_PORT=:8081 INF0554_COLOR=yellow ./demo &

green:
	INF0554_PORT=:8082 INF0554_COLOR=green ./demo &

stop:
	lsof -i :8080 | grep LISTEN | awk '{print $$2}' | xargs kill
	lsof -i :8081 | grep LISTEN | awk '{print $$2}' | xargs kill
	lsof -i :8082 | grep LISTEN | awk '{print $$2}' | xargs kill

.PHONY: run stop
