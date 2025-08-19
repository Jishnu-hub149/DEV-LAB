df <- data.frame(
  Name = c('Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Frank', 'Grace', 'Henry'),
  Age = c(25, 30, 35, NA, 28, 40, 22, 30),
  Gender = c('F', 'M', 'M', 'M', 'M', 'M', 'F', 'M'),
  Survived = c(0, 1, 0, 1, 1, 0, 1, 0),
  Fare = c(100.0, 110.0, 85.0, 75.0, 80.0, 90.0, 95.0, 70.0)
)
print("Initial Dataset:")
print(df)
df_cleaned <- na.omit(df)
df_cleaned <- unique(df_cleaned)
print("Cleaned Dataset:")
print(df_cleaned)
selected_columns <- df_cleaned[, c("Name", "Age", "Survived")]
print("Selected Columns (Name, Age, Survived):")
print(selected_columns)
filtered_rows <- subset(df_cleaned, Age > 30 & Survived == 0)
print("Filtered Rows (Age > 30 and Not Survived):")
print(filtered_rows)
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
} else {
  library(ggplot2)
}

ggplot(df_cleaned, aes(x = Age, y = Fare, color = as.factor(Survived))) +
  geom_point(size = 3) +
  labs(
    title = "Age vs Fare Colored by Survival",
    x = "Age",
    y = "Fare",
    color = "Survived"
  ) +
  theme_minimal()