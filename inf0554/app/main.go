package main

import (
	"html/template"
	"log"
	"net"
	"net/http"
	"os"
	"sync"
)

type Config struct {
	// Server attribs
	ListenPort string

	// Page attribs
	PageColor    string
	PageHostname string
    PageLocalIP       string
}

var (
	config *Config
	once   sync.Once

    colorMap = map[string]string{
        "blue":   "#87CEEB",
        "yellow": "#FFFACD",
        "green":  "#98FB98",
    }
)

func GetConfig() *Config {
    once.Do(func() {
        config = &Config{
            ListenPort: os.Getenv("INF0554_PORT"),
            PageColor:  os.Getenv("INF0554_COLOR"),
        }

        if config.ListenPort == "" {
            config.ListenPort = ":8080"
        }

        config.PageHostname, _ = os.Hostname()

        config.PageLocalIP = GetNetworkStatus()

        // Use color from env var if it exists, otherwise use blue
        if color, ok := colorMap[config.PageColor]; ok {
            config.PageColor = color
        } else {
            config.PageColor = colorMap["blue"]
        }
    })
    return config
}

func GetNetworkStatus() string {
    conn, err := net.Dial("udp", "8.8.8.8:80")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    return conn.LocalAddr().(*net.UDPAddr).IP.String()
}

func PageHandler(w http.ResponseWriter, r *http.Request) {
    data := GetConfig()
	template.Must(template.ParseFiles("src/page.html")).Execute(w, data)
}

func main() {
    config := GetConfig()

	// Create a new ServeMux
	mux := http.NewServeMux()

	// Setup routes
	mux.HandleFunc("GET /health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	})
	mux.HandleFunc("GET /", PageHandler)

	// Start the server
	log.Printf("Server is running on port %s\n", config.ListenPort)
	http.ListenAndServe(config.ListenPort, mux)
}
