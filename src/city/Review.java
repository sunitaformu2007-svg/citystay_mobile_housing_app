package city;

public class Review {
    private String reviewerID;
    private String userID;
    private int propertyID;
    private int rating;
    private String comment;

    public Review(String reviewerID, String userID, int propertyID, int rating, String comment) {
        this.reviewerID = reviewerID;
        this.userID = userID;
        this.propertyID = propertyID;
        this.rating = rating;
        this.comment = comment;
    }

    public void add_review() {
        // Logic to add the review to a database or data structure
        System.out.println("Review added by " + reviewerID + " for property " + propertyID);
    }

    public void edit_review() {
        // Logic to edit the review details
        System.out.println("Editing review by " + reviewerID + ": " + comment + " (Rating: " + rating + ")");
    }
}