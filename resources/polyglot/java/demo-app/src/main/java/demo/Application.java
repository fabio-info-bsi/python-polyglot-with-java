package demo;

import java.util.List;

public class Application {

    public List<String> findByUcodeBatch(final String ucode) {
        return List.of("A", "B", "C");
    }

    public int findById(final int id) {
        return id;
    }
}
