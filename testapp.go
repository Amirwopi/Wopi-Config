import (
    "context"
    "fmt"
	"time"
    "github.com/xxf098/lite-proxy/web"
)
// see more details in ./examples
func testPing() error {
    ctx := context.Background()
    link := "https://raw.githubusercontent.com/Amirwopi/Wopi-Config/main/splitted/channels"
    opts := web.ProfileTestOptions{
		GroupName:     "Default", 
		SpeedTestMode: "pingonly",   //  pingonly speedonly all
		PingMethod:    "googleping", // googleping
		SortMethod:    "rspeed", // speed rspeed ping rping
		Concurrency:   2,
		TestMode:      2,
		Subscription:  link,
		Language:      "en",  // en cn
		FontSize:      24,
		Theme:         "rainbow",
        Unique:        true,
		Timeout:       10 * time.Second,
		OutputMode:  0,
	}
    nodes, err := web.TestContext(ctx, opts, &web.EmptyMessageWriter{})
    if err != nil {
        return err
    }
    // get all ok profile
    for _, node := range nodes {
        if node.IsOk {
			fmt.Println(node.Remarks)
		}
	}
    return nil
}
