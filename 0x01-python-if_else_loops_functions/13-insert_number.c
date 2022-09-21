#include "lists.h"

/**
 * insert_node - it inserts a node in a sorted linked list
 * @head: double pointer to first node of linked list
 * @number: integer for the new node
 * Return: address of new node, or NULL upon failure
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new, *curr;
  
  curr = *head;

  new = malloc(sizeof(listint_t));
  if (!new || !head)
    return (NULL);
  new->n = number;
  new->next = NULL;

  if (*head == NULL || (*head)->n > number)
    {
      new->next = *head;
      *head = new;
      return (new);
    }
  while (curr->next != NULL)
    {
      if (curr->next->n > number)
	{
	  new->next = curr->next;
	  curr->next = new;
	  return (new);
	}
      curr = curr->next;
    }
  curr->next = new;
  return (new);
}
