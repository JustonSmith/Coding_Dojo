package java_stack.ProjectClass;

public class ProjectClass {
    private String Name;
    private String Description;
    private Double Cost;

    public String ElevatorPitch(){
        return (this.getName() + this.getDescription() + " ($" + Double.toString(getCost()) + ")");
    }

    public ProjectClass(){
        this.Name = "";
        this.Description = "";
        this.Cost = 0.00;
    }

    public ProjectClass(String projectName){
        this.Name = projectName;
        this.Description = "";
        this.Cost = 0.00;
    }

    public ProjectClass(String projectName, String projectDescription){
        this.Name = projectName;
        this.Description = projectDescription;
        this.Cost = 0.00;
    }

    public ProjectClass(String projectName, String projectDescription, Double projectCost){
        this.Name = projectName;
        this.Description = projectDescription;
        this.Cost = projectCost;
    }

    public void setName(String newName){
        this.Name = newName;
    }

    public void setDescription(String newDescription){
        this.Description = newDescription;
    }

    public void setCost(Double projectCost){
        this.Cost = projectCost;
    }

    public String getName(){
        return (Name);
    }

    public String getDescription(){
        return (Description);
    }

    public Double getCost(){
        return (Cost);
    }
}




