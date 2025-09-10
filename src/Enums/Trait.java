public enum Trait {
    NOCTURNAL("Nocturnal", "This role does something at night."),
    EXECUTIONER("Executioner", "This role is capable of killing without voting."),
    INVESTIGATOR("Investigator","This role learns information about other players."),
    SUBTLE("Subtle","This role’s ability does not trigger other roles, such as Night-Watch or Winderghiest."),
    HEAD_START("Head-Start","This role gains some benefit at the start of the game."),
    DEFENDER("Defender","This role does something in response to another role targeting them or this role’s target."),
    ALIBI("Alibi","This role is capable of revealing itself to the other players, confirming their role."),
    COPYCAT("Copycat","This role utilizes the abilities of other roles.");

    private final String name;
    private final String description;

    public Trait(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public String getName() { return name; }
    public String getDescription() { return description; }

    public boolean eqauls(String str) { return str.equals(this.name); }
    public boolean eqauls(Trait trait) { return equals(trait.getName()); }
}