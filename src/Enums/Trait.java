public enum Trait {
    NOCTURNAL("Nocturnal", "This role does something at night."),
    EXECUTIONER("Executioner", "This role is capable of killing without voting.");

    private final String name;
    private final String description;

    public Trait(String name, String description) {
        this.name = name;
        this.description = description;
    }
}