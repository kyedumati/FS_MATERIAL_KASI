package in.ksr.campushello;

import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public Map<String, String> hello() {
        // TODO: return JSON with a message for CampusCart
        return Map.of();
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        // TODO: return status UP (and optional app name)
        return Map.of();
    }
}
